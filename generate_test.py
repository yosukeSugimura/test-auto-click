import click
import requests
import openai
import base64
import yaml
from tqdm import tqdm  # プログレスバーを追加

# YAML設定ファイルの読み込み
def load_config():
    with open('config.yaml', 'r') as file:
        return yaml.safe_load(file)

# GitHub APIとOpenAI APIの設定を読み込み
config = load_config()
GITHUB_TOKEN = config['github']['token']
OPENAI_API_KEY = config['openai']['api_key']
openai.api_key = OPENAI_API_KEY

@click.command()
@click.option('--output', default='generated_test.php', help='生成されたテストケースを保存するファイルパス')
def generate_test(output):
    """YAML設定ファイルに基づいて、GitHubリポジトリのPHPコードからユニットテストを生成し、ファイルに保存します。"""
    
    owner = config['github']['owner']
    repo = config['github']['repo']
    path = config['paths']['php_file']

    # GitHubからPHPコードを取得する前にプログレスバーを表示
    with tqdm(total=3, desc="進捗", bar_format="{l_bar}{bar} [時間経過: {elapsed} / 残り: {remaining}]") as pbar:
        pbar.set_description("GitHubリポジトリからコードを取得中...")
        
        # GitHubからPHPコードを取得
        url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
        headers = {
            'Authorization': f'Bearer {GITHUB_TOKEN}',
            'Accept': 'application/vnd.github.v3+json'
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            content = response.json()
            # ファイルの内容はbase64でエンコードされているため、デコードする
            file_content = base64.b64decode(content['content']).decode('utf-8')
        else:
            click.echo(f'Error fetching code from GitHub: {response.status_code}')
            return
        
        pbar.update(1)  # 進捗バーを1つ進める

        # OpenAI APIを使ってPHPUnitのテストケースを生成
        pbar.set_description("OpenAI APIでテストケース生成中...")
        prompt = f"以下のPHPコードに対して、PHPUnitを使用したユニットテストを生成してください:\n\n{file_content}"

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )

        generated_test = response.choices[0].text.strip()
        pbar.update(1)  # 進捗バーをさらに進める

        # 生成されたテストケースをファイルに保存
        pbar.set_description(f"{output} にテストケースを書き込み中...")
        try:
            with open(output, 'w') as file:
                file.write(generated_test)
            click.echo(f"生成されたテストケースが {output} に保存されました。")
        except Exception as e:
            click.echo(f"ファイルの書き込みに失敗しました: {e}")
        
        pbar.update(1)  # 最後のステップを完了

if __name__ == '__main__':
    generate_test()

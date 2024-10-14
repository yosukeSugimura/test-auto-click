
# test-auto-click

`test-auto-click`は、特定の条件に基づいて自動でブラウザ上のクリック操作を行うツールです。このリポジトリは、主にUIテストの自動化や操作のエミュレーションを目的としています。

## 🚀 特徴

- **ブラウザ操作の自動化**: Playwrightを使用して、高速かつ信頼性の高い自動クリックを実現。
- **シンプルな設定**: 設定ファイルに操作の手順を記載するだけで実行可能。
- **拡張性の高い設計**: 将来的なシナリオ追加にも柔軟に対応。

## 🛠️ 使用技術

- **Node.js**
- **Playwright**
- **CodeceptJS** (バージョン 3.6.2)

## 📂 インストール手順

1. このリポジトリをクローンします。

   ```bash
   git clone https://github.com/yosukeSugimura/test-auto-click.git
   cd test-auto-click
   ```

2. 必要な依存パッケージをインストールします。

   ```bash
   npm install
   ```

3. `.env`ファイルにAPIキーや環境変数を設定します。  
   **例**:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## ▶️ 使用方法

1. 設定ファイル `config.yaml` を編集し、クリックシナリオを定義します。
2. 以下のコマンドで自動クリックを実行します。

   ```bash
   npm run auto-click
   ```

   **例:**  
   特定のページで要素をクリックする場合:
   ```yaml
   url: "https://example.com"
   actions:
     - click: "#button-id"
   ```

## 🔍 テストの実行

以下のコマンドでテストを実行します。

```bash
npx codeceptjs run --steps
```

## 🧑‍💻 開発者向け

このプロジェクトの開発者向けガイドラインです。

### 必要なツール

- Node.js 14+
- Playwright

### 開発中のヒント

- ブラウザの起動が必要な場合、以下のコマンドでPlaywrightのUIを表示できます。
  ```bash
  npx playwright show-trace
  ```

## 🚧 注意事項

- **APIキーの管理**: APIキーやその他の機密情報は、必ず`.env`ファイルで管理し、Gitにコミットしないようにしてください。

## 📄 ライセンス

このプロジェクトは [MITライセンス](LICENSE) のもとで提供されています。

## 🤝 コントリビューション

コントリビューションは大歓迎です！バグ報告や機能追加の提案は[Issues](https://github.com/yosukeSugimura/test-auto-click/issues)からお願いします。

## 📧 問い合わせ

何か質問があれば、[yosukeSugimura](https://github.com/yosukeSugimura)までご連絡ください。

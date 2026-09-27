# Test App

Spring Boot + Vue 3 + MySQL + Moto を使った簡易 Web アプリケーションです。  
ローカル開発用の認証、メモ管理、ToDo 管理、E2E テスト自動化をまとめて扱える構成になっています。

## 目次

- [プロジェクト概要](#プロジェクト概要)
- [技術スタック](#技術スタック)
- [ローカル開発環境](#ローカル開発環境)
- [起動方法](#起動方法)
- [テスト実行](#テスト実行)
- [CI / GitHub Actions](#ci--github-actions)
- [補足](#補足)

---

## プロジェクト概要

このリポジトリは、以下を目的としたサンプル実装です。

- バックエンド API の実装（Spring Boot）
- フロントエンド UI の実装（Vue 3 + Vite）
- MySQL による永続化
- AWS S3 相当のストレージを Moto でローカルエミュレーション
- Playwright による E2E テスト
- GitHub Actions による自動化

主な機能としては、次のような画面と API を想定しています。

- ユーザー認証
- メモ管理
- ToDo 管理

---

## 技術スタック

### バックエンド

- Java 17
- Spring Boot 3.5.9
- Spring Security
- Spring Data JPA
- MySQL 8.0
- AWS SDK for Java v2
- Gradle

### フロントエンド

- Vue 3.5.13
- Vite
- Vuetify 3.8.5
- Axios
- Playwright 1.52.0
- Allure 3.10.2

### インフラ

- Docker
- Docker Compose
- GitHub Actions
- Moto (S3 / AWS API エミュレーション)

> 重要: 実装上の S3 エミュレーションは LocalStack ではなく Moto を使用しています。

---

## ローカル開発環境

前提条件:

- Docker
- Docker Compose
- Git
- Node.js 20 系（推奨）
- Java 17

---

## 起動方法

### 1. リポジトリをクローン

```bash
git clone https://github.com/kamn-sap/test_app.git
cd test_app
```

### 2. Docker Compose で起動

```bash
cd infra
docker compose -f docker-compose.local.yml up -d --build
```

起動対象:

- MySQL: http://localhost:3306
- Backend: http://localhost:8080
- Frontend: http://localhost:5173
- Moto: http://localhost:5000

### 3. 動作確認

```bash
curl http://localhost:8080/actuator/health
```

ブラウザで `http://localhost:5173` を開いて利用します。

### 4. 停止

```bash
cd infra
docker compose -f docker-compose.local.yml down
```

---

## テスト実行

### E2E テスト

```bash
cd frontend
npm install
npx playwright test
```

### ユニットテスト

```bash
cd frontend
npm run test:unit
```

### Allure レポート

```bash
cd frontend
npx allure generate allure-results --clean -o allure-report
npx allure open allure-report
```

---

## CI / GitHub Actions

このリポジトリでは GitHub Actions で E2E テストを実行する構成を採用しています。

- 実行方法: 手動実行（workflow から実行）
- 主要対象: `.github/workflows/e2e.yml`
- データの検証や自動化は実装に合わせて運用します

---

## 補足

- 本リポジトリの S3 代替実装は LocalStack ではなく Moto です。
- wiki には補助的な設計メモや運用メモが含まれますが、実装を最優先にしてください。
- README は実装に沿ってメンテナンスされる前提です。

---

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。

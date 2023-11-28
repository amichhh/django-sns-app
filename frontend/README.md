# DJANGO SNSアプリ FRONTEND

## Vuetify3

- mdi-iconが表示されない。
  - 以下の手順で解決。
  1. @mdi/font をインストール
  - `npm install @mdi/font`
  2. main.ts に @mdi/font インポートを記述
  - `import '@mdi/font/css/materialdesignicons.css'`を追加

# DJANGO SNSアプリ BACKEND

## パッケージのインストール
- Django
  - Pythonのフレームワーク
  - `pip install django`
- Django REST framework(DRF)
  - REST APIバックエンド構築に特化したパッケージ
  - `pip install djangorestframework`
- CORS
  - Django REST FrameworkでCORSを設定するためのパッケージ
  - CORSとは？
    - `Cross-Origin Resource Sharing`の略で、オリジン間リソース共有のこと。
    - オリジンとは「プロトコル + ホスト(ドメイン) + ポート」で構成された、Webアプリケーションが動作している場所を表す。
    - セキュリティの観点から、リクエストを許可したオリジンからのみに制限するためCORSが利用されている。
    - → ポートまで完全に同じでないと別のオリジンとして認識されてしまうためアクセスできない
    - そのため、フロントエンドとバックエンドを切り離してAPI連携をするWebアプリケーション開発ではCORS設定が必要。
  - `pip install django-cors-headers`
  - `setting.py`で以下を設定する
    - ```
      INSTALLED_APPS = [
          ...
          'corsheaders',
      ]

      MIDDLEWARE = [
          ...
          'corsheaders.middleware.CorsMiddleware',
      ]

      CORS_ORIGIN_WHITELIST = [
          // アクセスを許可したいURLを追加
          'http://127.0.0.1:3000'
      ]
      ```

## DRF(Django REST Framework)
- Django REST Framework(DRF)は、PythonウェブフレームワークであるDjangoを補完する形で開発されたRESTful APIフレームワーク。
- DRFはDjangoをベースにしているため、Djangoの機能と特性を活用しながら、APIの作成や管理を簡単に行うことが可能。
- RESTfulなAPIを構築するために必要な機能やツールを提供し、開発者が効率的にAPIを実装できるように設計されている。

### View
- APIView
  - GETメソッド
    - パラメータは`request.query_params`で受け取る。
  - POSTメソッド
    - パラメータは`request.data`で受け取る。

### Serializer
- シリアライザとは、データの入出力を扱い、モデルへの橋渡しをするクラス。
  - （プレーンなDjangoには`Form`クラスがあるが、そのAPI用がシリアライザ。`Form`ではJSONやXMLのような複雑なデータは処理できないためAPI実装において過不足が多い）
  - `Serializer`は複雑な入力値をモデルに合わせてバリデーションしてレコードに伝えたり、Model(レコード)を適切な形式にフォーマットしたり、APIの リクエスト/レスポンスに特化した機能を利用できる。
  - シリアライズ: PythonオブジェクトをJSONファイルに変換
  - デシリアライズ: JSONファイルからPythonオブジェクトを生成
- シリアライザの種類
  - Serializer
    - もっとも単純なシリアライザ。
  - ModelSerializer
    - Modelに紐づくFieldをSerializerのフィールドとして自動的に定義する。
    - データが複数になる(list形式)場合は`many=True`引数を指定することでまとめて処理が可能。
      - `many=True`の有無により期待される型が異なる(辞書型orリスト型)ため注意。
      - ただし、保存処理は`create`や`update`を複数回実行しているに過ぎないため効率は良くない。
      - → `ListSerializer`を使う。
  - ListSerializer
    - 複数のモデルを扱うことを前提にしたシリアライザ。
    - `create`や`update`メソッドを省略した場合は`child`のシリアライザが要素の回数だけ呼び出される。

## 認証機能
  
## User
- `django.contrib.auth.models.User`がDjangoのユーザモデルで、これをインポートして使う。
- Userの主要な属性は以下の通り。
  - id
  - username
  - password
  - email
- Userを作成するには`create_user()`関数を使う。
  - `user = User.objects.create_user('username', 'foo@example.com', 'password')`

## *args, **kwargs
- 「可変長引数」と呼ぶ。
  - kwargs = `keyword arguments`の略。
  - 引数名には任意の名前を利用できるが、慣例として*args及び**kwargsが用いられることが多い。
- タプルと辞書型オブジェクトを扱える。

- *args
  - 複数の引数をタプルとして受け取る。
    - タプルとは、不変な配列を扱う型。定義後に要素を変更できない点でリストと異なる。
    - [] ではなく () を使用する。

- **kwargs
  - 複数のキーワード引数を辞書型オブジェクトとして受け取る。
    - 辞書型オブジェクトとは、キーと値をセットで扱うデータ型。

## Python命名規則
- クラス
  - 先頭大文字 + 大文字区切り
  - （例）`MyFavoriteClass`
- 例外
  - 先頭大文字 + 大文字区切り
  - （例）`MyFavoriteError`
- 型変数
  - 先頭大文字 + 大文字区切り
  - （例）`MyFavoriteType`
- メソッド
  - 全小文字 + アンダースコア区切り
  - （例）`my_favorite_method`
- 変数
  - 全小文字 + アンダースコア区切り
  - （例）`my_favorite_instance`
- 定数
  - 全大文字 + アンダースコア区切り
  - （例）`MY_FAVORITE_CONST`
from app import app, db
from models import Post, User  # 必要なモデルをインポート

with app.app_context():
    db.create_all()  # データベースとテーブルを再作成

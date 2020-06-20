from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbspartas  # 'dbspartas'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
## 주문하기 버튼 클릭시 주문목록에 추가>db에 저장
## 주문내역보기 > 페이지 로딩 후 자동으로 가져오기> 모두의 책리뷰
## 이름,수량,주소,저화번호 가져오고 db에 삽입하고 성공여부 반환
@app.route('/orders', methods=['POST'])
def write_order():
    name_receive = request.form['name_give']
    num_receive = request.form['num_give']
    ad_receive = request.form['ad_give']
    phone_receive = request.form['phone_give']

    order = {
       'name': name_receive,
       'num': num_receive,
       'ad': ad_receive,
       'phone': phone_receive
    }

    db.orders.insert_one(order)
    return jsonify({'result': 'success', 'msg': '주문내역이 성공적으로 작성되었습니다.'})

    


@app.route('/orders', methods=['GET'])
def read_orders():
    
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)



    ##


    
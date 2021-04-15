from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import uuid, json

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/api/home', methods=['GET'])
def home():
    home_page_articles = {
        "topicList": [{
            "id": 2,
            "title": "手手绘",
            "imgUrl": "http://upload.jianshu.io/collections/images/21/20120316041115481.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/64/h/64"
        }],
        "articleList": [{
            "id": 1,
            "title": "胡歌12年后首谈车祸",
            "desc": "文/麦大人 01 胡歌又刷屏了。 近日他上了《朗读者》，而这一期的主题是“生命”，他用磁性的嗓音，朗读了一段《哈姆雷特》中的经典独白，相当震撼：...",
            "imgUrl": "http://upload-images.jianshu.io/upload_images/2259045-2986b9be86b01f63?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240"
        }, {
            "id": 2,
            "title": "胡歌12年后首谈车祸：既然活下来了，就不能白白活着",
            "desc": "文/麦大人 01 胡歌又刷屏了。 近日他上了《朗读者》，而这一期的主题是“生命”，他用磁性的嗓音，朗读了一段《哈姆雷特》中的经典独白，相当震撼：...",
            "imgUrl": "http://upload-images.jianshu.io/upload_images/2259045-2986b9be86b01f63?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240"
        }, {
            "id": 3,
            "title": "胡歌12年后首谈车祸：既然活下来了，就不能白白活着",
            "desc": "文/麦大人 01 胡歌又刷屏了。 近日他上了《朗读者》，而这一期的主题是“生命”，他用磁性的嗓音，朗读了一段《哈姆雷特》中的经典独白，相当震撼：...",
            "imgUrl": "http://upload-images.jianshu.io/upload_images/2259045-2986b9be86b01f63?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240"
        }, {
            "id": 4,
            "title": "胡歌12年后首谈车祸：既然活下来了，就不能白白活着",
            "desc": "文/麦大人 01 胡歌又刷屏了。 近日他上了《朗读者》，而这一期的主题是“生命”，他用磁性的嗓音，朗读了一段《哈姆雷特》中的经典独白，相当震撼：...",
            "imgUrl": "http://upload-images.jianshu.io/upload_images/2259045-2986b9be86b01f63?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240"
        }],
        "recommendList": [{
            "id": 1,
            "imgUrl": "http://cdn2.jianshu.io/assets/web/banner-s-3-7123fd94750759acf7eca05b871e9d17.png"
        }, {
            "id": 2,
            "imgUrl": "http://cdn2.jianshu.io/assets/web/banner-s-5-4ba25cf5041931a0ed2062828b4064cb.png"
        }]
    }
    resp = {"success": True, "data": home_page_articles}
    rst = make_response(json.dumps(resp))
    return rst


@app.route('/api/homeList', methods=['GET'])
def home_list():
    home_articles = [{
        "id":
            5,
        "title":
            "胡歌12年后首谈车祸1",
        "desc":
            "文/麦大人 01 胡歌又刷屏了。 近日他上了《朗读者》，而这一期的主题是“生命”，他用磁性的嗓音，朗读了一段《哈姆雷特》中的经典独白，相当震撼：...",
        "imgUrl":
            "http://upload-images.jianshu.io/upload_images/2259045-2986b9be86b01f63?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240"
    }, {
        "id":
            6,
        "title":
            "胡歌12年后首谈车祸：既然活下来了，就不能白白活着2",
        "desc":
            "文/麦大人 01 胡歌又刷屏了。 近日他上了《朗读者》，而这一期的主题是“生命”，他用磁性的嗓音，朗读了一段《哈姆雷特》中的经典独白，相当震撼：...",
        "imgUrl":
            "http://upload-images.jianshu.io/upload_images/2259045-2986b9be86b01f63?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240"
    }]
    resp = {"success": True, "data": []}
    if request.args.get('page'):
        resp['data'] = [home_articles[int(request.args.get('page')) % 2]]
        rst = make_response(json.dumps(resp))
        return rst


@app.route('/api/headerList', methods=['GET'])
def header_list():
    header_list_articles = [
        "高考", "区块链", "三生三世", "崔永元", "vue", "小程序", "茶点微小说",
        "萨沙讲史堂", "夜幕下的地安门", "擦亮你的眼", "理财", "毕业", "手帐",
        "简书交友", "spring", "古风", "故事", "暖寄归人", "旅行", "连载", "教育",
        "简书",
        "生活", "投稿", "历史", "PHP", "考研", "docker", "EOS", "微信小程序",
        "PPT", "职场", "大数据", "创业", "书评", "东凤", "饱醉豚", "雨落荒原",
        "程序员", "爬虫", "时间管理", "kotlin", "数据分析", "阴阳合同", "设计",
        "红楼梦", "父亲节", "女人和衣服", "swift", "高考作文"]

    resp = {"success": True, "data": header_list_articles}
    rst = make_response(json.dumps(resp))
    return rst


@app.route('/api/login', methods=['GET'])
def login():
    rst = make_response(json.dumps({
        "success": True,
        "data": True
    }))
    return rst


@app.route('/api/detail', methods=['GET'])
def detail():
    if request.args.get('id'):
        print(request.args.get('id'))
    resp = {
        "success": True,
        "data": {
            "title": "衡水中学，被外地人占领的高考工厂",
            "content": "衡水中学，被外地人占领的高考工厂 content"
        }}
    rst = make_response(json.dumps(resp))
    return rst


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3001)

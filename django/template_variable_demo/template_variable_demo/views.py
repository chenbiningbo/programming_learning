from django.shortcuts import render

# class person(object):
#     def __init__(self, username):
#         self.username = username

def index(request):

    # context = {
    #     'age': 17
    # }
    # context ={
    #     'heros':[
    #         '鲁班一号',
    #         '项羽',
    #         '程咬金'
    #     ]
    # }
    context = {
        # 'books': [
        #     '三国演义',
        #     '水浒传',
        #     '西游记',
        #     '红楼梦'
        # ],
        'person': {
            'username': 'zhiliao',
            'age': 18,
            'height':180
        },

        'books': [
            {
                'name': '三国演义',
                'author': '罗贯中',
                'price': 199
            },
            {
                'name': '水浒传',
                'author':'施耐庵',
                'price': 89
            },
            {
                'name': '西游记',
                'author': '吴承恩',
                'price': 129
            },
            {
                'name':'红楼梦',
                'author': '曹雪芹',
                'price': 178
            }
        ],
        'comments': [

        ]

    }
    return render(request, 'index.html', context = context)
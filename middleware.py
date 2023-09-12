def my_middleware(ge_response):
    print('init 被调用')

    def middleware(request):
        print('request 被调用')
        response=ge_response(request)
        print('reponse 被调用')
        return response

    return middleware
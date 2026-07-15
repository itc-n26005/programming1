def show_kwargs(**kwargs):
    '''与えられた複数のキーワード引数を辞書にまとめて受け取りその辞書を表示して返す'''
    print('Keyword arguments:', kwargs)
    return kwargs

print(show_kwargs(pasta='ペンネ', drink='赤ワイン', main_dish='肉料理', n_customers=3))

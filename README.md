# lecture_polymphys_randomwalk

講義「高分子物理学特論」の#2「Scaling Law of Ideal Chains」、#3「Scaling Law of Real Chains」で利用

＜未解決問題＞  
まだrw/distinctwalk系をgitしてない  
まだsaw/distinctwalk系もgitしてない

＜distinctwalkについて＞  
git上では  
distinct_walks --> v0
distinct_walks_r1 --> v1  
distinct_walks_r2 --> v2  
とリネームしてpushしてある。v2の最後のバージョンはほとんど完成系なので"_v2"と名前を変更するだけにする。

＜np.ndarrayに置き換える試み＞  
pythonのリストで書いたオリジナルをnp.ndarrayに置き換える試みを行った。  
以下は完了済み  
rw/animation/1d  
rw/animation/2d  
rw/statistics/1d  
その結果、statisticsのところでnp.ndarrayの方が圧倒的に遅いと分かったので、  
さらにtimeitを使って時間を計測してみた  
rw/animation/1d/randomWalk_1d_speedTest_anim.py  
rw/statistics/1d/randomWalk_1d_speedTest_stat.py  
その結果、  
list =  0.029663904100016226  
array =  0.0016563124998356215  
でarrayの方が圧倒的に速いが、no_imgでやると  
list_noimg =  3.56917007593438e-05  
でlistの方が圧倒的に速いという結論になった。  
以下の記事  
<https://teratail.com/questions/219411>  
によると、  
> 普通にpythonレイヤからnumpy配列の「要素」にアクセスするような処理をすると、オーバーヘッドの塊みたいなものですから遅い

とのこと。まさにそれなのかなと結論づいた。  

以上のことから、「np.ndarrayに置き換える試み」は凍結することとした。  
ただし、見栄えの問題で  
from matplotlib import animation  
を使うのではなく、  
import animatplot as amp  
を使う方には変えたい（3dはNGだけど）ので、その修正だけ行うことを実行開始（250218）。  

実行完了（250221）、これに合わせてstatisticsの方も少しいじる  
その過程で    
np.random.choice  
が遅いということ、  
rng = np.random.default_rng()  
rng.choice()  
も速くはないということが判明したので、statisticsの方は  
rd.choice  
に戻すことにした。  

これに関する未解決問題として  
rw/animation/3d  
animatplotは3次元描画ができない。  
3次元のアニメーションは従来のmatplotlibのanimation.ArtistAnimationを使うしかない

＜過去の更新履歴＞（開発の手順の記録として残しておく）
更新履歴

１．rw（random walk）とsaw（self-avoiding walk）にまず分離している。

２，それぞれのフォルダ内で
	「animation」フォルダ内のプログラム
			経路の様子を全て書き出すために乱数発生で経路を作っている。
			それぞれの経路に相関はない。
			同じ経路が選ばれる可能性もある。
	「statistics」フォルダ内のプログラム
			「animation」フォルダ内のプログラムをベースにスナップショットを撮れる。
			かつさまざまな統計処理も行い、授業で用いたバージョン。

	「animation」と「statistics」で計算されている経路、おかしいかもしれない。要チェック。
	「animation」の方は大丈夫だと思われる。

	「distinct_walks」フォルダ内のプログラム
			例えば「rw1dCoordinate」でN stepの経路を発生させ、「rw1dDistinctWalks」で異なる経路を排除している。
			このため区別可能な全ての経路の総数を算出できる。が、検索に時間がかかり、N < 10にとどまる。
	「distinct_walks_r1」フォルダ内のプログラム
			発想を大きく変え、「rw1dAddStep」などで各ステップごとの経路リストを作成する方向に転換した。
			「rw1dDistinctWalks」で異なる経路の排除も行っている。
			「distinct_walks」フォルダ内のプログラムよりは若干速くなったが、それほど変化なしだった。
	「distinct_walks_r2」フォルダ内のプログラム
			ランダムに次のステップを与えるのではなく、決まったブランチ数を繰り返すだけに変更。
			またそれに伴い、「distinct_walks_r2」で行っていた、「rw1dDistinctWalks」での異なる経路の排除も不要に。
			かなり速くなったが、指数関数的に増える経路数には勝てない。

３．更にその下に「1d」「2d」「3d」でプログラムを分けている

上でおかしいと思ったのは、以下の部分。
       x_list.append(x) #ステイすることを示すためには必要、最終経路示すだけなら不要
       y_list.append(y) #ステイすることを示すためには必要、最終経路示すだけなら不要
これを追加するとanimationするときに、そこにステイしていることがわかりやすくなる。
一方、x_listやy_listの数がステイしている分増えるのでN = 10に原点を加えた(N + 1)よりも
多くなる。numは変更していないので、それでも最終的に得られるステップ数は問題ないし、r2を
計算する際もx_list[-1]等で行っているので問題ないはず。

つまりプログラムは正常。

220106追記

時間計測（time_count.py）をしながらどのくらい大変かを改めて計算してみることにした。
ログはメモに貼り付けて、複数マシンの情報を共有することにした。

情報はメモを利用している。

220310追記

iCloud上のpythonプログラムが常に最新になるようにキープするようにした。

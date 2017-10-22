# -*- coding: UTF-8 -*-

import web
import urllib, urllib2, json
import os, sys

#help(web.Storage)
# 设置默认编码
reload(sys)
sys.setdefaultencoding('utf-8')
print u"当前默认编码：" + sys.getdefaultencoding()

# 连接数据库
# db = ControlMySQL.ControlMySQL(host = "127.0.0.1", user = "PyRoot", passwd = "root", db = "Database")

# 设置模板路径
root = os.path.dirname(__file__)
render = web.template.render(os.path.join(root, 'templates/'))
static_dir = os.path.join(root, 'static/')

# 设置当前工作目录
os.chdir(sys.path[0])

urls = (
    '/','index',
    '/movie/(\d+)','movie',
)

class index:
    def GET(self):
        return render.index()

class movie:
    def GET(self, movie):
        movie = int(movie)
        referer = web.ctx.env.get('HTTP_REFERER', 'http://google.com')
        print referer
        #web.seeother(referer)
        return render.movie(movie)

class static:
    def GET(self, static):
        print "hahahah" + static
        return web.seeother(static_dir + static)


# 404
def notfound():
    return web.notfound("Sorry, the page you were looking for was not found.")

# 500
def internalerror():
    return web.internalerror("Bad, bad server. No donut for you.")




if __name__ == "__main__":
    #显示调试信息
    #web.config.debug = False

    app = web.application(urls, globals())
    app.internalerror = internalerror
    app.notfound = notfound
    application = app.wsgifunc()
    #app.run()

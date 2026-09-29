[app]

title = Family IPO Tracker
package.name = familyipotracker
package.domain = org.chauhan

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,atlas,db

version = 1.0

requirements = python3,kivy==2.3.1,kivymd==2.0.0,materialyoucolor==3.0.3,materialshapes,asynckivy,asyncgui,pillow,pycairo,sqlite3
icon.filename = %(source.dir)s/app_icons.png
presplash.filename = %(source.dir)s/app_icons.png

orientation = portrait
fullscreen = 0


android.archs = arm64-v8a


[buildozer]

log_level = 2
warn_on_root = 1

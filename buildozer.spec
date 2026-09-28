[app]

title = Family IPO Tracker
package.name = familyipotracker
package.domain = org.chauhan

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,atlas,db

version = 1.0

requirements = python3,kivy,kivymd

orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/finrec_logo.png

android.archs = arm64-v8a

android.permissions =


[buildozer]

log_level = 2
warn_on_root = 1

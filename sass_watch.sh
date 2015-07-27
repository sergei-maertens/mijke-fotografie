#!/usr/bin/env sh
sassc -w \
    -I src/mijke/static/bower_components/bourbon/app/assets/stylesheets/ \
    -I src/mijke/static/bower_components/neat/app/assets/stylesheets/ \
    -I src/mijke/static/bower_components/bitters/app/assets/stylesheets/ \
    src/mijke/sass/screen.scss \
    src/mijke/static/screen.css \

// requirements

var gulp = require('gulp');
var gulpSass = require('gulp-sass');
var gulpBrowser = require("gulp-browser");
var reactify = require('reactify');
var del = require('del');
var size = require('gulp-size');

// tasks

gulp.task('transform', function () {
  var stream = gulp.src('./src/static/scripts/jsx/*.js')
    .pipe(gulpBrowser.browserify({transform: ['reactify']})
    .on('error', onError))
    .pipe(gulp.dest('./src/static/scripts/build/'))
    .pipe(size());
  return stream;
});

gulp.task('styles', function() {
  var stream = gulp.src('./src/static/styles/scss/*.scss')
    .pipe(gulpSass().on('error', gulpSass.logError))
    .pipe(gulp.dest('./src/static/styles/build'))
    .pipe(size());
  return stream;
})

gulp.task('del', function () {
  return del(['./src/static/scripts/build', './src/static/styles/build']);
});

gulp.task('default', ['del'], function () {
  gulp.start('transform');
  gulp.start('styles');
  gulp.watch('./src/static/scripts/jsx/*.js', ['transform']);
  gulp.watch('./src/static/styles/scss/*.scss', ['styles']);
});

function onError(err) {
  console.log(err);
  this.emit('end');
}
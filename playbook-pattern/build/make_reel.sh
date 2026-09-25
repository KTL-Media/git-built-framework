#!/bin/bash
# Build animated GIT BUILT carousel reel: Ken Burns per slide + crossfades + grade
set -e
D="$HOME/workspace/your_files/git-built-carousel"
cd "$D"
mkdir -p clips

i=1
for n in 01 02 03 04 05 06 07 08 09 10; do
  if [ $((i % 2)) -eq 1 ]; then
    ZEXPR="min(1.0+0.0009*on\,1.10)"      # push in
  else
    ZEXPR="max(1.10-0.0009*on\,1.0)"      # pull out
  fi
  ffmpeg -y -v error -loop 1 -i "gb-slide-$n.png" \
    -vf "scale=2160:2700,zoompan=z='${ZEXPR}':d=90:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1350:fps=30" \
    -t 3 -c:v libx264 -preset medium -pix_fmt yuv420p "clips/c$n.mp4"
  i=$((i+1))
done

INPUTS=""
for n in 01 02 03 04 05 06 07 08 09 10; do INPUTS="$INPUTS -i clips/c$n.mp4"; done

FILTER="[0:v][1:v]xfade=transition=fade:duration=0.6:offset=2.4[v1]"
for k in 2 3 4 5 6 7 8 9; do
  off=$(awk "BEGIN{printf \"%.1f\", 2.4*$k}")
  FILTER="${FILTER};[v$((k-1))][${k}:v]xfade=transition=fade:duration=0.6:offset=${off}[v${k}]"
done
FILTER="${FILTER};[v9]vignette=PI/4.2,noise=alls=5:allf=t,format=yuv420p[vout]"

ffmpeg -y -v error $INPUTS -filter_complex "$FILTER" -map "[vout]" \
  -c:v libx264 -preset medium -crf 18 -movflags +faststart gitbuilt-carousel-reel.mp4
echo "REEL DONE:"
ls -la gitbuilt-carousel-reel.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 gitbuilt-carousel-reel.mp4

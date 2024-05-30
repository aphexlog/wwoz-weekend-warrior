!/bin/sh
echo "Scrubbing WWOZ for weekend schedules"
python scripts/wwoz/wwoz.py

echo "Cleaning up data with AI"
for filename in ./scripts/wwoz/calendar_data/*.html; do
    echo "Processing $filename"
    python scripts/ai/ai.py "$filename"
done

response_files=(./scripts/ai/response_data/*)
echo ${response_files[0]}
jq -s '{Artists: (.[0].Artists + .[1].Artists + .[2].Artists)}' ${response_files[0]} ${response_files[1]} ${response_files[2]} > ./scripts/ai/response_data/combined_response.json

echo "Building spotify playlist"

python scripts/spotify/spotify.py

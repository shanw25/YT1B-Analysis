#!/bin/zsh

# Install GCS CLI before executing.

if [ $# -ne 1 ]; then
  echo "Usage: $0 <metadata_directory>"
  exit 1
fi

METADATA_DIR="$1"

if [ ! -d "$METADATA_DIR" ]; then
  echo "Error: The metadata directory '$METADATA_DIR' does not exist."
  exit 1
fi

START=0
END=1024

source $HOME/google-cloud-sdk/path.zsh.inc
source $HOME/google-cloud-sdk/completion.zsh.inc

# If not working, uncomment the lines above and Download GCS under $HOME dir. Then execute again.

for ((i=START; i<=END; i++))
do
    FILE_NUM=$(printf "%04d" $i)
    FILE_NAME="yttemporal1b_train_${FILE_NUM}of1024.jsonl.gz"
    gsutil cp gs://merlot/yttemporal1b/train_annotations/${FILE_NAME} "$METADATA_DIR"

    sleep 1
done
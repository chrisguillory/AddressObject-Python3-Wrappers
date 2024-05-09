DQS_DIR=dqs.202305
#DQS_DIR=dqs.202404

GEOCOM_DIR=GeoCOM.202401
#GEOCOM_DIR=GeoCOM.202404

docker run \
    --platform linux/amd64 \
    --volume /Users//chris/melissa_data:/melissa_data:ro \
    --volume ${PWD}:/app:ro \
    --rm \
    --workdir /app \
    --env LD_LIBRARY_PATH="/melissa_data/${DQS_DIR}/address/linux/gcc48_64bit:/melissa_data/${GEOCOM_DIR}/linux/gcc48_64bit" \
    python:3.11.2 \
    python -m main

#    -it \
#    --entrypoint bash \

# docker build -t gpu_burn .

ARG CUDA_VERSION=11.8.0
ARG IMAGE_DISTRO=ubi8

FROM nvidia/cuda:${CUDA_VERSION}-devel-${IMAGE_DISTRO} AS builder

WORKDIR /build

COPY . /build/

RUN make

FROM nvidia/cuda:${CUDA_VERSION}-runtime-${IMAGE_DISTRO}

COPY --from=builder /build/gpu_burn /app/
COPY --from=builder /build/compare.ptx /app/

WORKDIR /app

RUN mkdir -p /app/data

CMD ["sh", "-c", "./gpu_burn 10 > /app/data/gpu_status.txt"]
# CMD ["sh", "-c", "./gpu_burn 40"]

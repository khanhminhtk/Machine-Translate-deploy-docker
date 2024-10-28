FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /home/HPC

# Update package list and install dependencies
RUN apt-get update && \
    apt-get install -y software-properties-common python3 python3-pip python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Activate the virtual environment and install Python packages
RUN /opt/venv/bin/pip install --no-cache-dir torch==2.4.1+cu121 torchvision torchaudio \
    --index-url https://download.pytorch.org/whl/cu121 && \
    /opt/venv/bin/pip install --no-cache-dir transformers==4.44.2 flask

# Set the virtual environment as the default Python environment
ENV PATH="/opt/venv/bin:$PATH"

# Copy application code and models
COPY App ./App
COPY Model ./Model
COPY App.py ./App.py
COPY Etract_data.py ./Etract_data.py
COPY Load_model.py ./Load_model.py
COPY translate_en_to_vi.py ./translate_en_to_vi.py
COPY tokenizer_en ./tokenizer_en
COPY tokenizer_vi ./tokenizer_vi

CMD ["python3", "App.py"]
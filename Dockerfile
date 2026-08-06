#ARG IMAGE=intersystemsdc/irishealth-community
#ARG IMAGE=intersystemsdc/iris-community:preview
#ARG IMAGE=intersystemsdc/iris-community
ARG IMAGE=intersystemsdc/iris-community:latest
FROM $IMAGE

WORKDIR /home/irisowner/dev

ARG TESTS=0
ARG MODULE="iris-GenLab"
ARG NAMESPACE="USER"


# create Python env
## Embedded Python environment
## Python stuff
ENV IRISUSERNAME "SuperUser"
ENV IRISPASSWORD "SYS"
ENV IRISNAMESPACE "IRISAPP"
ENV PYTHON_PATH=/usr/irissys/bin/
ENV LD_LIBRARY_PATH=${ISC_PACKAGE_INSTALLDIR}/bin:${LD_LIBRARY_PATH}
ENV PATH "/usr/irissys/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/irisowner/bin:/home/irisowner/.local/bin"
ENV FILE_READ_PATH /home/irisowner/dev/input
COPY . .
## Start IRIS
RUN pip3 install -r requirements.txt --timeout 600 --retries 10
RUN python3 -c "import nltk; nltk.download('punkt_tab'); nltk.download('averaged_perceptron_tagger')"
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu --timeout 300
RUN iris start IRIS && \
    iris merge IRIS merge.cpf && \
    irispython iris_script.py && \
    iris stop IRIS quietly



#ENTRYPOINT [ "irispython", "python/app.py" ]
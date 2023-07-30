FROM python
RUN mkdir /py1
COPY cal.py/py1/
CMD ["python3","/py1/cal.py"]

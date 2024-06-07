#如果不是使用了N卡。且安装了cuda，请使用device=cpu
yolo detect train data=3.dataset.yaml model=yolov8n.pt epochs=100 device=0
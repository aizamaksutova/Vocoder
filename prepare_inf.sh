pip install gdown


gdown 1uv039ldvZz_4sCSebTT50bFCAl814jcb
echo "model loaded"

gdown https://drive.google.com/u/0/uc?id=1WsibBTsuRg_SF2Z6L6NFRTT-NjEy1oTx
mkdir -p hw_tts/waveglow/pretrained_model/
mv waveglow_256channels_ljs_v2.pt hw_tts/waveglow/pretrained_model/waveglow_256channels.pt
echo "waveglow done"

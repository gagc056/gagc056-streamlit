{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d8f932fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: streamlit in /home/gagc056/.local/lib/python3.11/site-packages (1.22.0)\n",
      "Requirement already satisfied: altair<5,>=3.2.0 in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (4.2.2)\n",
      "Requirement already satisfied: blinker>=1.0.0 in /usr/lib/python3/dist-packages (from streamlit) (1.4)\n",
      "Requirement already satisfied: cachetools>=4.0 in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (5.3.0)\n",
      "Requirement already satisfied: click>=7.0 in /usr/lib/python3/dist-packages (from streamlit) (8.0.3)\n",
      "Requirement already satisfied: importlib-metadata>=1.4 in /usr/lib/python3/dist-packages (from streamlit) (4.6.4)\n",
      "Requirement already satisfied: numpy in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (1.24.3)\n",
      "Requirement already satisfied: packaging>=14.1 in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (23.1)\n",
      "Requirement already satisfied: pandas<3,>=0.25 in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (2.0.1)\n",
      "Requirement already satisfied: pillow>=6.2.0 in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (9.5.0)\n",
      "Requirement already satisfied: protobuf<4,>=3.12 in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (3.20.3)\n",
      "Requirement already satisfied: pyarrow>=4.0 in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (12.0.0)\n",
      "Requirement already satisfied: pympler>=0.9 in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (1.0.1)\n",
      "Requirement already satisfied: python-dateutil in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: requests>=2.4 in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (2.30.0)\n",
      "Requirement already satisfied: rich>=10.11.0 in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (13.3.5)\n",
      "Requirement already satisfied: tenacity<9,>=8.0.0 in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions>=3.10.0.0 in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (4.5.0)\n",
      "Requirement already satisfied: tzlocal>=1.1 in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: validators>=0.2 in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (0.20.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19 in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (3.1.31)\n",
      "Requirement already satisfied: pydeck>=0.1.dev5 in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (0.8.1b0)\n",
      "Requirement already satisfied: tornado>=6.0.3 in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (6.3.2)\n",
      "Requirement already satisfied: watchdog in /home/gagc056/.local/lib/python3.11/site-packages (from streamlit) (3.0.0)\n",
      "Requirement already satisfied: entrypoints in /home/gagc056/.local/lib/python3.11/site-packages (from altair<5,>=3.2.0->streamlit) (0.4)\n",
      "Requirement already satisfied: jinja2 in /home/gagc056/.local/lib/python3.11/site-packages (from altair<5,>=3.2.0->streamlit) (3.1.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in /home/gagc056/.local/lib/python3.11/site-packages (from altair<5,>=3.2.0->streamlit) (4.17.3)\n",
      "Requirement already satisfied: toolz in /home/gagc056/.local/lib/python3.11/site-packages (from altair<5,>=3.2.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in /home/gagc056/.local/lib/python3.11/site-packages (from gitpython!=3.1.19->streamlit) (4.0.10)\n",
      "Requirement already satisfied: pytz>=2020.1 in /home/gagc056/.local/lib/python3.11/site-packages (from pandas<3,>=0.25->streamlit) (2023.3)\n",
      "Requirement already satisfied: tzdata>=2022.1 in /home/gagc056/.local/lib/python3.11/site-packages (from pandas<3,>=0.25->streamlit) (2023.3)\n",
      "Requirement already satisfied: six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil->streamlit) (1.16.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in /home/gagc056/.local/lib/python3.11/site-packages (from requests>=2.4->streamlit) (3.1.0)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /home/gagc056/.local/lib/python3.11/site-packages (from requests>=2.4->streamlit) (2.10)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /home/gagc056/.local/lib/python3.11/site-packages (from requests>=2.4->streamlit) (2.0.2)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /home/gagc056/.local/lib/python3.11/site-packages (from requests>=2.4->streamlit) (2023.5.7)\n",
      "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in /home/gagc056/.local/lib/python3.11/site-packages (from rich>=10.11.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /home/gagc056/.local/lib/python3.11/site-packages (from rich>=10.11.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: decorator>=3.4.0 in /usr/lib/python3/dist-packages (from validators>=0.2->streamlit) (4.4.2)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in /home/gagc056/.local/lib/python3.11/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit) (5.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in /home/gagc056/.local/lib/python3.11/site-packages (from jinja2->altair<5,>=3.2.0->streamlit) (2.1.2)\n",
      "Requirement already satisfied: attrs>=17.4.0 in /usr/lib/python3/dist-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit) (21.2.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /home/gagc056/.local/lib/python3.11/site-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit) (0.19.3)\n",
      "Requirement already satisfied: mdurl~=0.1 in /home/gagc056/.local/lib/python3.11/site-packages (from markdown-it-py<3.0.0,>=2.2.0->rich>=10.11.0->streamlit) (0.1.2)\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "eabfd8f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2023-05-23 01:11:55.936 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /home/gagc056/.local/lib/python3.10/site-packages/ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "ename": "RuntimeError",
     "evalue": "Runtime hasn't been created!",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "File \u001b[0;32m/usr/local/lib/python3.10/dist-packages/streamlit/elements/image.py:361\u001b[0m, in \u001b[0;36mimage_to_url\u001b[0;34m(image, width, clamp, channels, output_format, image_id)\u001b[0m\n\u001b[1;32m    360\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 361\u001b[0m     \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mimage\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mrb\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[1;32m    362\u001b[0m         image_data \u001b[38;5;241m=\u001b[39m f\u001b[38;5;241m.\u001b[39mread()\n",
      "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'banner-picture.jpeg'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[5], line 102\u001b[0m\n\u001b[1;32m    100\u001b[0m a,b,c \u001b[38;5;241m=\u001b[39m st\u001b[38;5;241m.\u001b[39mcolumns([\u001b[38;5;241m0.2\u001b[39m,\u001b[38;5;241m0.6\u001b[39m,\u001b[38;5;241m0.2\u001b[39m])\n\u001b[1;32m    101\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m b:\n\u001b[0;32m--> 102\u001b[0m  \u001b[43mst\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mimage\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mbanner-picture.jpeg\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43muse_column_width\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43;01mTrue\u001b[39;49;00m\u001b[43m)\u001b[49m\n\u001b[1;32m    105\u001b[0m \u001b[38;5;66;03m# description about the project and code files       \u001b[39;00m\n\u001b[1;32m    106\u001b[0m st\u001b[38;5;241m.\u001b[39msubheader(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m🧾Description:\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[0;32m/usr/local/lib/python3.10/dist-packages/streamlit/runtime/metrics_util.py:332\u001b[0m, in \u001b[0;36mgather_metrics.<locals>.wrapped_func\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    330\u001b[0m         _LOGGER\u001b[38;5;241m.\u001b[39mdebug(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFailed to collect command telemetry\u001b[39m\u001b[38;5;124m\"\u001b[39m, exc_info\u001b[38;5;241m=\u001b[39mex)\n\u001b[1;32m    331\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 332\u001b[0m     result \u001b[38;5;241m=\u001b[39m \u001b[43mnon_optional_func\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    333\u001b[0m \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[1;32m    334\u001b[0m     \u001b[38;5;66;03m# Activate tracking again if command executes without any exceptions\u001b[39;00m\n\u001b[1;32m    335\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m ctx:\n",
      "File \u001b[0;32m/usr/local/lib/python3.10/dist-packages/streamlit/elements/image.py:169\u001b[0m, in \u001b[0;36mImageMixin.image\u001b[0;34m(self, image, caption, width, use_column_width, clamp, channels, output_format)\u001b[0m\n\u001b[1;32m    166\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m StreamlitAPIException(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mImage width must be positive.\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m    168\u001b[0m image_list_proto \u001b[38;5;241m=\u001b[39m ImageListProto()\n\u001b[0;32m--> 169\u001b[0m \u001b[43mmarshall_images\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m    170\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdg\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_get_delta_path_str\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    171\u001b[0m \u001b[43m    \u001b[49m\u001b[43mimage\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    172\u001b[0m \u001b[43m    \u001b[49m\u001b[43mcaption\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    173\u001b[0m \u001b[43m    \u001b[49m\u001b[43mwidth\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    174\u001b[0m \u001b[43m    \u001b[49m\u001b[43mimage_list_proto\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    175\u001b[0m \u001b[43m    \u001b[49m\u001b[43mclamp\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    176\u001b[0m \u001b[43m    \u001b[49m\u001b[43mchannels\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    177\u001b[0m \u001b[43m    \u001b[49m\u001b[43moutput_format\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    178\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    179\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mdg\u001b[38;5;241m.\u001b[39m_enqueue(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mimgs\u001b[39m\u001b[38;5;124m\"\u001b[39m, image_list_proto)\n",
      "File \u001b[0;32m/usr/local/lib/python3.10/dist-packages/streamlit/elements/image.py:536\u001b[0m, in \u001b[0;36mmarshall_images\u001b[0;34m(coordinates, image, caption, width, proto_imgs, clamp, channels, output_format)\u001b[0m\n\u001b[1;32m    533\u001b[0m         is_svg \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mTrue\u001b[39;00m\n\u001b[1;32m    535\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m is_svg:\n\u001b[0;32m--> 536\u001b[0m     proto_img\u001b[38;5;241m.\u001b[39murl \u001b[38;5;241m=\u001b[39m \u001b[43mimage_to_url\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m    537\u001b[0m \u001b[43m        \u001b[49m\u001b[43mimage\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mwidth\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mclamp\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mchannels\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43moutput_format\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mimage_id\u001b[49m\n\u001b[1;32m    538\u001b[0m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m/usr/local/lib/python3.10/dist-packages/streamlit/elements/image.py:371\u001b[0m, in \u001b[0;36mimage_to_url\u001b[0;34m(image, width, clamp, channels, output_format, image_id)\u001b[0m\n\u001b[1;32m    368\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m mimetype \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m    369\u001b[0m     mimetype \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mapplication/octet-stream\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m--> 371\u001b[0m url \u001b[38;5;241m=\u001b[39m \u001b[43mruntime\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget_instance\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241m.\u001b[39mmedia_file_mgr\u001b[38;5;241m.\u001b[39madd(image, mimetype, image_id)\n\u001b[1;32m    372\u001b[0m caching\u001b[38;5;241m.\u001b[39msave_media_data(image, mimetype, image_id)\n\u001b[1;32m    373\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m url\n",
      "File \u001b[0;32m/usr/local/lib/python3.10/dist-packages/streamlit/runtime/__init__.py:29\u001b[0m, in \u001b[0;36mget_instance\u001b[0;34m()\u001b[0m\n\u001b[1;32m     25\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mget_instance\u001b[39m() \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m Runtime:\n\u001b[1;32m     26\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Return the singleton Runtime instance. Raise an Error if the\u001b[39;00m\n\u001b[1;32m     27\u001b[0m \u001b[38;5;124;03m    Runtime hasn't been created yet.\u001b[39;00m\n\u001b[1;32m     28\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[0;32m---> 29\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mRuntime\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43minstance\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m/usr/local/lib/python3.10/dist-packages/streamlit/runtime/runtime.py:146\u001b[0m, in \u001b[0;36mRuntime.instance\u001b[0;34m(cls)\u001b[0m\n\u001b[1;32m    142\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124;03m\"\"\"Return the singleton Runtime instance. Raise an Error if the\u001b[39;00m\n\u001b[1;32m    143\u001b[0m \u001b[38;5;124;03mRuntime hasn't been created yet.\u001b[39;00m\n\u001b[1;32m    144\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m    145\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mcls\u001b[39m\u001b[38;5;241m.\u001b[39m_instance \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m--> 146\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mRuntime hasn\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mt been created!\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m    147\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mcls\u001b[39m\u001b[38;5;241m.\u001b[39m_instance\n",
      "\u001b[0;31mRuntimeError\u001b[0m: Runtime hasn't been created!"
     ]
    }
   ],
   "source": [
    "# import all the app dependencies\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import sklearn\n",
    "import streamlit as st\n",
    "import joblib\n",
    "import matplotlib\n",
    "from IPython import get_ipython\n",
    "from PIL import Image\n",
    "\n",
    "# load the encoder and model object\n",
    "model = joblib.load(\"rta_model_deploy3.joblib\")\n",
    "encoder = joblib.load(\"ordinal_encoder2.joblib\")\n",
    "\n",
    "st.set_option('deprecation.showPyplotGlobalUse', False)\n",
    "\n",
    "# 1: serious injury, 2: Slight injury, 0: Fatal Injury\n",
    "\n",
    "st.set_page_config(page_title=\"Accident Severity Prediction App\",\n",
    "        page_icon=\"🚧\", layout=\"wide\")\n",
    "\n",
    "#creating option list for dropdown menu\n",
    "options_day = ['Sunday', \"Monday\", \"Tuesday\", \"Wednesday\", \"Thursday\", \"Friday\", \"Saturday\"]\n",
    "options_age = ['18-30', '31-50', 'Over 51', 'Unknown', 'Under 18']\n",
    "\n",
    "# number of vehicle involved: range of 1 to 7\n",
    "# number of casualties: range of 1 to 8\n",
    "# hour of the day: range of 0 to 23\n",
    "\n",
    "options_types_collision = ['Vehicle with vehicle collision','Collision with roadside objects',\n",
    "              'Collision with pedestrians','Rollover','Collision with animals',\n",
    "              'Unknown','Collision with roadside-parked vehicles','Fall from vehicles',\n",
    "              'Other','With Train']\n",
    "\n",
    "options_sex = ['Male','Female','Unknown']\n",
    "\n",
    "options_education_level = ['Junior high school','Elementary school','High school',\n",
    "              'Unknown','Above high school','Writing & reading','Illiterate']\n",
    "\n",
    "options_services_year = ['Unknown','2-5yrs','Above 10yr','5-10yrs','1-2yr','Below 1yr']\n",
    "\n",
    "options_acc_area = ['Other', 'Office areas', 'Residential areas', ' Church areas',\n",
    "    ' Industrial areas', 'School areas', ' Recreational areas',\n",
    "    ' Outside rural areas', ' Hospital areas', ' Market areas',\n",
    "    'Rural village areas', 'Unknown', 'Rural village areasOffice areas',\n",
    "    'Recreational areas']\n",
    "\n",
    "# features list\n",
    "features = ['Number_of_vehicles_involved','Number_of_casualties','Hour_of_Day','Type_of_collision','Age_band_of_driver','Sex_of_driver',\n",
    "    'Educational_level','Service_year_of_vehicle','Day_of_week','Area_accident_occured']\n",
    "\n",
    "# Give a title to web app using html syntax\n",
    "st.markdown(\"<h1 style='text-align: center;'>Accident Severity Prediction App 🚧</h1>\", unsafe_allow_html=True)\n",
    "\n",
    "# define a main() function to take inputs from user in form based approach\n",
    "def main():\n",
    "    with st.form(\"road_traffic_severity_form\"):\n",
    "       st.subheader(\"Please enter the following inputs:\")\n",
    "        \n",
    "       No_vehicles = st.slider(\"Number of vehicles involved:\",1,7, value=0, format=\"%d\")\n",
    "       No_casualties = st.slider(\"Number of casualties:\",1,8, value=0, format=\"%d\")\n",
    "       Hour = st.slider(\"Hour of the day:\", 0, 23, value=0, format=\"%d\")\n",
    "       collision = st.selectbox(\"Type of collision:\",options=options_types_collision)\n",
    "       Age_band = st.selectbox(\"Driver age group?:\", options=options_age)\n",
    "       Sex = st.selectbox(\"Sex of the driver:\", options=options_sex)\n",
    "       Education = st.selectbox(\"Education of driver:\",options=options_education_level)\n",
    "       service_vehicle = st.selectbox(\"Service year of vehicle:\", options=options_services_year)\n",
    "       Day_week = st.selectbox(\"Day of the week:\", options=options_day)\n",
    "       Accident_area = st.selectbox(\"Area of accident:\", options=options_acc_area)\n",
    "        \n",
    "       submit = st.form_submit_button(\"Predict\")\n",
    "\n",
    "# encode using ordinal encoder and predict\n",
    "    if submit:\n",
    "       input_array = np.array([collision,\n",
    "                  Age_band,Sex,Education,service_vehicle,\n",
    "                  Day_week,Accident_area], ndmin=2)\n",
    "        \n",
    "       encoded_arr = list(encoder.transform(input_array).ravel())\n",
    "        \n",
    "       num_arr = [No_vehicles,No_casualties,Hour]\n",
    "       pred_arr = np.array(num_arr + encoded_arr).reshape(1,-1)        \n",
    "      \n",
    "# predict the target from all the input features\n",
    "       prediction = model.predict(pred_arr)\n",
    "        \n",
    "       if prediction == 0:\n",
    "           st.write(f\"The severity prediction is fatal injury⚠\")\n",
    "       elif prediction == 1:\n",
    "           st.write(f\"The severity prediction is serious injury\")\n",
    "       else:\n",
    "           st.write(f\"The severity prediction is slight injury\")\n",
    "        \n",
    "       st.write(\"Developed By: Avi kumar Talaviya\")\n",
    "       st.markdown(\"\"\"Reach out to me on: [Twitter](https://twitter.com/avikumart_) |\n",
    "       [Linkedin](https://www.linkedin.com/in/avi-kumar-talaviya-739153147/) |\n",
    "       [Kaggle](https://www.kaggle.com/avikumart) \n",
    "       \"\"\")\n",
    "\n",
    "a,b,c = st.columns([0.2,0.6,0.2])\n",
    "with b:\n",
    " st.image(\"banner-picture.jpeg\", use_column_width=True)\n",
    "\n",
    "\n",
    "# description about the project and code files       \n",
    "st.subheader(\"🧾Description:\")\n",
    "st.text(\"\"\"This data set is collected from Addis Ababa Sub-city police departments for master's research work. \n",
    "The data set has been prepared from manual records of road traffic accidents of the year 2017-20. \n",
    "All the sensitive information has been excluded during data encoding and finally it has 32 features and 12316 instances of the accident.\n",
    "Then it is preprocessed and for identification of major causes of the accident by analyzing it using different machine learning classification algorithms.\n",
    "\"\"\")\n",
    "\n",
    "st.markdown(\"Source of the dataset: [Click Here](https://www.narcis.nl/dataset/RecordID/oai%3Aeasy.dans.knaw.nl%3Aeasy-dataset%3A191591)\")\n",
    "\n",
    "st.subheader(\"🧭 Problem Statement:\")\n",
    "st.text(\"\"\"The target feature is Accident_severity which is a multi-class variable. \n",
    "The task is to classify this variable based on the other 31 features step-by-step by going through each day's task. \n",
    "The metric for evaluation will be f1-score\n",
    "\"\"\")\n",
    "\n",
    "st.markdown(\"Please find GitHub repository link of project: [Click Here](https://github.com/avikumart/Road-Traffic-Severity-Classification-Project)\")          \n",
    "  \n",
    "# run the main function        \n",
    "if __name__ == '__main__':\n",
    "  main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ad15a10",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

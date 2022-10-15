# BundleImageGenerator
Stack multiple images from a URL into a single image. Perfect for the Hydra Vaults generated NFTBundle from Pluto Pawn. 
Support for +2 NFT Bundle

<p align="center">
  <img src="https://github.com/DegenDwarfs/BungleImageGenerator/blob/main/img/examples/2.png" width="200">
  <img src="https://github.com/DegenDwarfs/BungleImageGenerator/blob/main/img/examples/3.png" width="200">
  <img src="https://github.com/DegenDwarfs/BungleImageGenerator/blob/main/img/examples/6.png" width="200">
</p>


## Install Dependencies
windows powershell:
```powershell
py -m pip install -r requirements.tx
```
Linux:
```console
pip install -r requirements.tx
```

## Setup Script
Before you can run `main.py` you will need to run the `setup.py` script.
windows powershell:
```powershell
py setup.py
```
Linux:
```console
python setup.py
```

## Run Demo
Generate a demo bundle, using `test_nft_data` as the test array of tokenURI links and `demo_bundle_id` as the demo `bundle_id`.
You should see a file named `69.png` generated in `bundles_dir` (`./bunldes/`)
windows powershell:
```powershell
py -m main.py demo
```
Linux:
```console
python main.py demo
```

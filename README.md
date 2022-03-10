# AutoDC: Automated data-centric processing

[![GitHub license](https://img.shields.io/github/license/gohypeegiant/AutoDC)](https://github.com/gohypergiant/AutoDC/blob/main/LICENSE.txt)

This repository is the official Python implementation of position paper "AutoDC: Automated data-centric processing". The implementation will continue being updated in the coming months. Note that only image data is supported.

![image](Fig_1.png)

AutoDC is a framework to enable domain experts to automatically and systematically improve datasets without much coding requirement and manual process, the idea similar with AutoML (automated machine learning).

By using the AutoML system, such as Google Cloud AutoML, domain experts only need to bring in the input data, and AutoML takes care of the manual ML processes, then produces output predictions, along with user-defined evaluation metrics. With a similar idea, AutoDC is designed for domain experts to bring in a labeled dataset, such as annotated images, to the system; AutoDC takes care of the manual data improvement processes, and produces the improved dataset, by automatically correcting the incorrect labels (with user feedbacks), detecting edge cases, and augmenting edge cases.

<br>

**Full Paper**:<br>
Zac Yung-Chun Liu, Shoumik Roychowdhury, Scott Tarlow, Akash Nair, Shweta Badhe, and Tejas Shah. AutoDC: Automated data-centric processing, NeurIPS 2021: DCAI workshop, [arXiv: 2111.12548](https://arxiv.org/abs/2111.12548).

## Dependencies

- `opencv-python` >= 4.5.3.56
- `scikit-learn` >= 0.24.2
- `numpy` >= 1.19.5
- `python-magic-bin` >= 0.4.14
- `augly` >= 0.2.1

You also need Python >= 3.6.

## Install

`pip install` using the `requirements.txt`:

```shell
pip install -r requirements.txt
```

## Getting Started

1. Using starter script `starter_image_data.py`, you only need to provide the directory path that has input images and the directory path that the output images (improved dataset) will be stored.

```shell
python starter_image_data.py --input Users/sample_data/ --output Users/sample_data/
```

Optional, you can also specify:
- `--o_ratio`: outlier data ratio, default: `10`
- `--n_ratio`: non outlier data ratio, default: `40`
- `--a_ratio`: augmented data ratio, default: `20`

2. Using starter notebook `starter_image_data.ipynb`, just follow the steps.

## License

`AutoDC` is released under Apache 2.0 License.

## Citation

See our paper describing the framework:

Zac Yung-Chun Liu, Shoumik Roychowdhury, Scott Tarlow, Akash Nair, Shweta Badhe, and Tejas Shah (2021), "[AutoDC: Automated data-centric processing](https://arxiv.org/abs/2111.12548)", *arXiv:2111.12548*

```bibtex
@misc{liu2021autodc,
      title={AutoDC: Automated data-centric processing},
      author={Zac Yung-Chun Liu and Shoumik Roychowdhury and Scott Tarlow and Akash Nair and Shweta Badhe and Tejas Shah},
      year={2021},
      eprint={2111.12548},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

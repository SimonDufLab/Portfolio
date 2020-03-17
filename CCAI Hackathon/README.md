## Remarks

This notebook was set up during the CCAI hackathon, september 2019.

The goal of the current model is to be predict correctly the number of stories
of a building based on a Google StreetView images.

The notebook is self-contained : Images can be retrieved from StreetView by
entering an address.

The model itself is a pre-trained dataset that was refined on a dataset
extracted from StreetView (building images) and cross-referenced with public
data to retrieved the number of stories.

Model : Mobile-Net V2, tensorflow implementation.

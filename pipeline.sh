#!/bin/bash

set -e
python="/usr/local/anaconda3/bin/python"

src="/home/epaillasv/Dropbox/data/eboss_v5/code"
src_SVF="/home/epaillasv/code/SVF_survey_delaunay/bin"

zlo=0.6
zhi=1.1
nden=3e-3
data_ang_fits="/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/eBOSS_ELG_clustering_NGC_v5.dat.fits"
data_car_ascii="/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/eBOSS_ELG_clustering_NGC_v5.dat.car.txt"
data_ang_ascii="/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/eBOSS_ELG_clustering_NGC_v5.dat.ang.txt"
random_ang_fits="/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/eBOSS_ELG_clustering_NGC_v5.ran.fits"
random_car_ascii="/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/eBOSS_ELG_clustering_NGC_v5.ran.car.txt"
random_ang_ascii="/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/eBOSS_ELG_clustering_NGC_v5.ran.ang.txt"
random_sphere_ang="/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/rnd_sphere_ELG_NGC_nden3e-3.npy"
redCap_ang="/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/eBOSS_ELG_clustering_NGC_v5.redCap.ang.npy"
redCap_car="/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/eBOSS_ELG_clustering_NGC_v5.redCap.car.npy"
angCap_ang="/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/eBOSS_ELG_clustering_NGC_v5.angCap.ang.npy"
angCap_car="/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/eBOSS_ELG_clustering_NGC_v5.angCap.car.npy"
dataguards_car="/home/epaillasv/data/eboss_v5/test_pipeline/void_cats/eBOSS_ELG_clustering_NGC_v5.dat+Cap.car.npy"
delaunay_ver_car="/home/epaillasv/data/eboss_v5/test_pipeline/void_cats/eBOSS_ELG_clustering_NGC_v5.ver.car.txt"
delaunay_cen_car="/home/epaillasv/data/eboss_v5/test_pipeline/void_cats/eBOSS_ELG_clustering_NGC_v5.cen.car.txt"
delaunay_cen_ang="/home/epaillasv/data/eboss_v5/test_pipeline/void_cats/eBOSS_ELG_clustering_NGC_v5.cen.ang.txt"
delaunay_cenin_ang="/home/epaillasv/data/eboss_v5/test_pipeline/void_cats/eBOSS_ELG_clustering_NGC_v5.cenin.ang.txt"
delaunay_cenin_car="/home/epaillasv/data/eboss_v5/test_pipeline/void_cats/eBOSS_ELG_clustering_NGC_v5.cenin.car.txt"


# # Convert angular fits catalogues to angular ascii catalogues
# $python $src/fits_to_ascii.py $data_ang_fits $data_ang_ascii
# $python $src/fits_to_ascii.py $random_ang_fits $random_ang_ascii
#
# # Convert angular ascii catalogues to cartesian ascii catalogues
# $python $src/angular_to_cartesian.py $data_ang_ascii $data_car_ascii
# $python $src/angular_to_cartesian.py $random_ang_ascii $random_car_ascii
#
# Generate random sphere with 5 times the nden of data catalogye
$python $src/generate_random_sphere.py $random_sphere_ang $random_ang_ascii $zlo $zhi $nden

# Generate angular and redshift caps with mock buffer particles
$python $src/generate_guard_particles.py $random_ang_ascii $random_sphere_ang $redCap_ang $angCap_ang $zlo $zhi

# Convert buffer particles to cartesian coordinates
$python $src/angular_to_cartesian.py $redCap_ang $redCap_car
$python $src/angular_to_cartesian.py $angCap_ang $angCap_car

# Join buffer particles and data catalogue
$python $src/join_guards_and_data.py $data_car_ascii $angCap_car $redCap_car $dataguards_car

# Run a Delaunay triangulation on the data+buffer galaxies
$python $src_SVF/delaunay_triangulation.py $dataguards_car $delaunay_ver_car

# Find circumcentres of Delaunay triangles
$src_SVF/circumsphere.exe $delaunay_ver_car $delaunay_cen_car

# Convert circumcentres to angular coordinates
$python $src/cartesian_to_angular.py $delaunay_cen_car $delaunay_cen_ang

# Filter centres by survey mask
$python $src/filter_by_survey_mask.py $delaunay_cen_ang $delaunay_cenin_ang $random_ang_ascii $zlo $zhi

# Convert centres back to cartesian coordinates
$python $src/angular_to_cartesian.py $delaunay_cenin_ang $delaunay_cenin_car

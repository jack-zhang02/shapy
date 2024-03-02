# !! IMPORTANT !!

Ok so this is forked from an open source repository muelea/shapy which provides most of the crunchy stuff. The main "new stuff" is in "loop.py" or "loop_gpt.py" depending on your prefernce. Getting the body shape estimation, measurements, and attribute estimations are all basically using the demo scripts provided, for which the main off-the-shelf python files are:

shapy/regressor/demo.py
shapy/measurements/virtual_measurements.py

TODOs include making loop.py better and finishing matcher.py which goes from the loop.py outputs to a set of matches in the csv bratabase.

There are some installations and checks that you will have to do beforehand which are below.

## datasets

Firstly, go to shapy/data in terminal. Then run the following, and when the user/pw prompt comes up, use jzhang0@sas.upenn.edu and Mintman123! respectively.

```
urle () { [[ "${1}" ]] || return 1; local LANG=C i x; for (( i = 0; i < ${#1}; i++ )); do x="${1:i:1}"; [[ "${x}" == [a-zA-Z0-9.~-] ]] && echo -n "${x}" || printf '%%%02X' "'${x}"; done; echo; }

read -p "Username:" username
read -p "Password:" -s password

username=$(urle $username)
password=$(urle $password)

# SHAPY
wget --post-data "username=$username&password=$password" 'https://download.is.tue.mpg.de/download.php?domain=shapy&resume=1&sfile=shapy_data.zip' -O 'shapy_data.zip' --no-check-certificate --continue
unzip shapy_data.zip
rm shapy_data.zip
```

Then do the same (again jzhang0@sas.upenn.edu and Mintman123! ) for the following, still in shapy/data:

```

urle () { [[ "${1}" ]] || return 1; local LANG=C i x; for (( i = 0; i < ${#1}; i++ )); do x="${1:i:1}"; [[ "${x}" == [a-zA-Z0-9.~-] ]] && echo -n "${x}" || printf '%%%02X' "'${x}"; done; echo; }

read -p "Username:" username
read -p "Password:" -s password

username=$(urle $username)
password=$(urle $password)

# SMPL-X
wget --post-data "username=$username&password=$password" 'https://download.is.tue.mpg.de/download.php?domain=smplx&sfile=models_smplx_v1_1.zip&resume=1' -O 'models_smplx_v1_1.zip' --no-check-certificate --continue
unzip models_smplx_v1_1.zip
mv models body_models
rm models_smplx_v1_1.zip
```

Then continue by:

```
ln -s shapy/regressor/samples/shapy_fit shapy/samples/shapy_fit
```

And it should be all set. Some thing might also break and be fixable by looking at the muelea/shapy original repository and its issues, the authors are still kind of active.


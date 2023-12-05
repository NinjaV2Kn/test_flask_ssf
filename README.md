# SSF
<h1>A fridge that reads how many drinks are in it, and mesures things like the temperature etc.</h1>
<h2>requirements:</h2>
* Raspberry Pi</br>
* 16 Buttons and wires</br>
* 2 Nanoleaf sets(6 for the count and one other set)</br>
<h2>setup:</h2>
1. Download the files to your raspberry pi
2. change the IP adresses in Nanoleaf.py and in payLeaf.py
3. connect your buttons to the right GPIO Pins(you can see the right pin in BottleSensors.py)
4. if you want to use the PayPal counter you have to make an endpoint for it and change the url in bottlesSold.py
5. create a venv in the main SSF folder and activate it.
6. now install the requirements.
7. start it with "python Main.py"

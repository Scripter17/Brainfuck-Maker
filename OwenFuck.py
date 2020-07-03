# OwenFuck - An alias of BrainFuck using 8 words given by my friend Owen
import bfm

bf=bfm.BrainFuck(
	{
		"um":bfm.defaultBF.addOp,
		"poo":bfm.defaultBF.subOp,
		"barack obama":bfm.defaultBF.incOp,
		"skinny":bfm.defaultBF.decOp,
		"joj":bfm.defaultBF.outOp, # He probably meant "jojo", but he said to keep it like this
		"jesus":[bfm.defaultBF.loopB, "minecraft"]
	},
	{
		"tape":[0 for x in range(30000)],
		"pointer":0
	}
)
code=["um","jesus","poo","jesus","skinny","skinny","jesus","um","jesus","poo","poo","poo","barack obama","minecraft","poo","jesus","skinny","skinny","skinny","minecraft","minecraft","minecraft","barack obama","barack obama","barack obama","poo","minecraft","barack obama","poo","joj","poo","poo","poo","joj","barack obama","joj","joj","barack obama","joj","skinny","skinny","skinny","skinny","poo","joj","skinny","um","joj","barack obama","barack obama","barack obama","barack obama","barack obama","joj","barack obama","joj","skinny","skinny","joj","skinny","poo","joj"]
bf.run(code)

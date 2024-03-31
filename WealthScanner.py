import os 
import anvil #Need to use this library because minecraft has a stupid format for their files
from nbt import nbt

#All the region files, they should end with .mca

def iter(currentWorld):
    item_data = {}
    with open((currentWorld + ".txt"), "w") as f:
        regionFiles = os.listdir("./worlds/"+currentWorld+"/region")
        for file in regionFiles:
            region = anvil.Region.from_file("./worlds/"+currentWorld+"/region/"+(file))
            for x in range(32):
                for z in range(32) :
                    try: 
                        chunk = region.get_chunk(x,z)
                    except Exception:
                        continue
                    for tile_entity in chunk.tile_entities:
                        try:
                            items = tile_entity["Items"]
                            for item in items:
                                item_data[5] = item["id"]
                                try:
                                    #name of the itemstack, needed for items like chetherite and titanium, where both's ID is Minecraft:iron_ingot
                                    #In a try block because sometimes it doesnt have a name
                                    item_data[5] = item["tag"]["display"]["Name"]
                                except Exception: 1    
                                item_data[0]= tile_entity["x"].value #X coord
                                item_data[1] = tile_entity["y"].value #Y coord
                                item_data[2] = tile_entity["z"].value #Z coord
                                item_data[3]= item["id"].value #Minecraft ID for the block, ex: Minecraft:Dirt
                                item_data[4]= item["Count"].value #Number in the itemstack
                                #Write the invenformation for this itemStack to a new line
                                f.write(f"Inventory at coordinates ({item_data[0]}, {item_data[1]},{item_data[2]}, of {item_data[3]}, count: {item_data[4]}, name: {item_data[5]})")
                                f.write("\n")
                                print(f"Inventory at coordinates ({item_data[0]}, {item_data[1]},{item_data[2]}, of {item_data[3]}, count: , name: {item_data[5]})")
                        except Exception:
                            continue
    print("finished") 
                    
worlds = os.listdir("./worlds")
for world in worlds:
    iter(world)

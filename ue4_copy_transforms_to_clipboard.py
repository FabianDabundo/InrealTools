import bpy, math, os
from __main__ import *

#-------------------------------------------------------
#*****write transforms into string*****
#-------------------------------------------------------
transforms=(
'Begin Map\n'
'   ''Begin Level\n')

for obj in bpy.context.selected_objects:
    transforms=transforms+(
'      ''Begin Actor Class=StaticMeshActor Name='+obj.name+' Archetype=StaticMeshActor\'/Script/Engine.Default__StaticMeshActor\'\n'
'         ''Begin Object Class=StaticMeshComponent Name=\"StaticMeshComponent0\" Archetype=StaticMeshComponent\'Default__StaticMeshActor:StaticMeshComponent0\'\n'
'         ''End Object\n'
'         ''Begin Object Name=\"StaticMeshComponent0\"\n'
'            ''StaticMesh=StaticMesh\'/Engine/EditorMeshes/EditorCube.EditorCube\'\n'
'            ''RelativeLocation=(X='+str(obj.location.x*100)+',Y='+str(-obj.location.y*100)+',Z='+str(obj.location.z*100)+')\n'
'            ''RelativeScale3D=(X='+str(obj.scale.x)+',Y='+str(obj.scale.y)+',Z='+str(obj.scale.z)+')\n'
'            ''RelativeRotation=(Pitch='+str(obj.rotation_euler.y/2/math.pi*360)+',Yaw='+str(obj.rotation_euler.z/2/math.pi*360)+',Roll='+str(obj.rotation_euler.x/2/math.pi*360)+')\n'
'            ''CustomProperties\n'
'         ''End Object\n'
'         ''StaticMeshComponent=StaticMeshComponent0\n'
'         ''Components(0)=StaticMeshComponent0\n'
'         ''RootComponent=StaticMeshComponent0\n'
'         ''ActorLabel=\"'+obj.name+'\"\n'
'      ''End Actor\n')

transforms=transforms+(
'   ''End Level\n'
'Begin Surface\n'
'End Surface\n'
'End Map\n')


#-------------------------------------------------------
#*****create textfile with transformationdata of selected objects that UE4 can read*****
#-------------------------------------------------------
#blenderCipher=open('C:\\Users\\fabia\\Desktop\\selection.txt','w')
#blenderCipher.write(transforms)
#blenderCipher.close()


#-------------------------------------------------------
#*****copy transforms to clipboard*****
#-------------------------------------------------------
bpy.context.window_manager.clipboard=transforms


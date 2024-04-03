sudo apt install openjdk-21-jdk
mkdir minecraft
cd minecraft
mkdir mods
curl -L https://download.geysermc.org/v2/projects/floodgate/versions/latest/builds/latest/downloads/spigot --output geyser.jar
curl -L https://api.papermc.io/v2/projects/paper/versions/1.20.4/builds/463/downloads/paper-1.20.4-463.jar --output paper.jar
echo eula=true > eula
mv geyser.jar mods
java -Xmx4G -Xms4G -jar paper.jar --nogui
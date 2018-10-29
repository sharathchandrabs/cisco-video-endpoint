from flask import Flask, render_template, jsonify
import xml.etree.ElementTree as ET
import logging
app = Flask(__name__)

class ParseXML():

	def __init__(self,filename):
		self.tree = ET.parse(filename)
	def parsexml(self,elem, parsed_dict):
		if len(elem)> 0:
			for item in elem:
                 		self.parsexml(item, parsed_dict)
         	else:
             		parsed_dict[elem.tag] =  elem.text
		return parsed_dict

@app.route('/')
def index():
	parser = ParseXML('status.xml')
	
	final_dict = {}
	sysUnit = parser.tree.findall('SystemUnit')
	final_dict['System Unit'] = parser.parsexml(sysUnit, {})

	
	peripherals = parser.tree.findall('Peripherals')
	cDevices = []
	for items in peripherals:
		connected_devices = items.findall('ConnectedDevice')

		for devices in connected_devices:
			conType = devices.find('Type')
			app.logger.info(conType.text)
			if conType.text == 'Camera':
				cDevices.append(devices)
	
	dev_list = []
	for devs in cDevices:
		dev_list.append(parser.parsexml(devs, {}))

	final_dict['Peripherals'] = dev_list
	app.logger.info(final_dict)
	call = parser.tree.findall('Call')
	final_dict['Call'] = parser.parsexml(call, {})

	network = parser.tree.findall('Network')
	final_dict['Network'] = parser.parsexml(network, {})

	time = parser.tree.findall('Time')
	final_dict['Time'] = parser.parsexml(time, {})
	
	
	userInterface = parser.tree.findall('UserInterface')
	final_dict['Contact'] = parser.parsexml(userInterface, {})
	return render_template('index.html', final_dict = final_dict)


if __name__ == '__main__':
	app.run(debug=True)

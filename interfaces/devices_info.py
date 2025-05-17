class DeviceData:
	def __init__(self, name, status):
		self.name = name
		self.status = status

	def getStatus(self):
		return "Prendida" if self.status else "Apagada"

class RecorderDeviceData(DeviceData):
	def __init__(self, name, status, isRecording):
		super().__init__(name, status)
		self.isRecording = isRecording

class TempratureDeviceData(DeviceData):
	def __init__(self, name, status, temprature):
		super().__init__(name, status)
		self.temprature = temprature
import sublime, sublime_plugin, re

class HtointCommand(sublime_plugin.EventListener):
	def on_new(self, view):
		self.view = view
		self.run()

	def on_close(self, view):
		self.view.erase_status('Hexcode')

	def on_selection_modified(self, view):
		self.view = view
		self.run()

	def on_activated(self, view):
		self.view = view
		self.run()

	def run(self):
		statusline = []
		for region in self.view.sel():
			if region.begin() == region.end():
				word = self.view.word(region)
			else:
				word = region
			if not word.empty():
				keyword = self.view.substr(word)
				isHex = re.findall(r'0x[0-9a-fA-F]+', keyword)
				# print(isHex)
				if isHex:
					statusline.append('{} -> {}'.format(isHex[0], self.str_to_int(isHex[0])))
				else:
					self.view.erase_status('Hexcode')
			else:
				self.view.erase_status('Hexcode')
		# print(", ".join(statusline))
		self.view.set_status('Hexcode', '{}'.format(", ".join(statusline)))

	def str_to_int(self, s):
		i = int(s, 16)
		if i >= 2**23:
			i -= 2**24
		return i



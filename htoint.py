import sublime, sublime_plugin, re

class HtointCommand(sublime_plugin.EventListener):
	def on_new(self, view):
		self.run(view)

	def on_selection_modified(self, view):
		self.run(view)

	def on_activated(self, view):
		self.run(view)

	def run(self, view):
		statusline = []
		for region in view.sel():
			
			if region.begin() == region.end():
				word = view.word(region)
			else:
				word = region

			if not word.empty():

				keyword = view.substr(word)
				isHex = re.findall(r'0x[0-9a-fA-F]+', keyword)

				if isHex:
					statusline.append('{} -> {}'.format(isHex[0], self.str_to_int(isHex[0])))

		view.erase_status('Hexcode')
		view.set_status('Hexcode', '{}'.format(", ".join(statusline)))

	def str_to_int(self, s):
		i = int(s, 16)
		if i >= 2**23:
			i -= 2**24
		return i



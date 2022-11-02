import lection_4_model
import lection_4_view


def butt_click():
	val_a = lection_4_view.get_val()
	val_b = lection_4_view.get_val()
	lection_4_model.init(val_a, val_b)
	result = lection_4_model.sum()
	lection_4_view.view_data(result)
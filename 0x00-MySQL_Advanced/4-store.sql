-- Create a trigger to decrease the quantity of an item after adding a new order
CREATE TRIGGER update_items AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name=NEW.item_name;

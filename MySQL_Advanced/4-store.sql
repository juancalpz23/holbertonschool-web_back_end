-- Script to create a trigger for updating item quantity after a new order

DELIMITER //

CREATE TRIGGER decrease_item_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.quantity
    WHERE id = NEW.item_id;
END //

DELIMITER ;

#from app.database import db, ma


#class Base(db.Model):

#    __abstract__ = True

#    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


#class Order(Base):
#    """
#    Create as Order table
#    """

#    __tablename__ = 'order'

#    number = db.Column(db.String(20))
#    date = db.Column(db.DateTime)


#class OrderDetail(Base):
#    """
#    Create as Order Detail table
#    """

#    __tablename__ = 'order_detail'

#    description = db.Column(db.String(250))
#    price = db.Column(db.Numeric(16, 2))
#    quantity = db.Column(db.Integer)
#    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
#    order = db.relationship('Order')


#class OrderSchema(ma.ModelSchema):
#    class Meta:
#        model = Order


#class OrderDetailSchema(ma.ModelSchema):
#    class Meta:
#        model = OrderDetail

class Productos:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        productos=self.session.get("productos")
        if not productos:
            productos=self.session["productos"]={}
        #else:
        self.productos= productos

    def agregar(self, producto):
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id]={
                "producto_id":producto.id,
                "titulo": producto.titulo,
                "descripcion": producto.descripcion,
                "precio": str(producto.precio),
                "imagen":producto.imagen.url
            }
        else:
            for key, value in self.productos.items():
                if key==str(producto.id):
                    break
        self.guardar_productos()

    def guardar_productos(self):
        self.session["carro"]=self.productos
        self.session.modified=True

    def eliminar(self, producto):
        producto_id=str(producto.id)
        if producto_id in self.productos:
            del self.productos[producto_id]
            self.guardar_productos()


namespace GuitarShop.Models
{
    public class Product
    {
        public int ProductID { get; set; }
        public string Name { get; set; }
        public decimal Price { get; set; }
        public string Availability { get; set; }
        public string Slug => Name.Replace(' ', '-');
    }
}
from rest_framework import serializers
from models.base_models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'slug', 'name', 'price', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ["id"]

    def _get_or_create_tags(self, tags, recipe):
        """Handle getting or creating tags as needed."""
        auth_user = self.context['request'].user
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(
                user=auth_user,
                **tag,
            )
            recipe.tags.add(tag_obj)


class ProductDetailSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + ['description']
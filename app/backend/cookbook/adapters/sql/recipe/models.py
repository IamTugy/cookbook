from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column

from cookbook.adapters.sql.base import Base
from cookbook.adapters.sql.user.models import User

from cookbook.domain.recipe.models import Recipe as DomainRecipe, RecipeAdditionalInformation, \
    Instruction as DomainInstruction, SimpleStep, TimeStep

instructions_to_ingredients = Table(
    "instructions_to_ingredients",
    Base.metadata,
    Column("instruction_id", ForeignKey("instructions.id")),
    Column("ingredient_id", ForeignKey("ingredients.id")),
)


class RatingVote(Base):
    __tablename__ = "rating_votes"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user: Mapped[User] = relationship(back_populates="rating_votes")
    rating: Mapped[int] = mapped_column()


class Ingredient(Base):
    __tablename__ = "ingredients"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column()
    calories: Mapped[int] = mapped_column()  # calories per 100 grams
    instructions: Mapped[list["Instruction"]] = relationship(secondary=instructions_to_ingredients,
                                                             back_populates="ingredients")


class Instruction(Base):
    __tablename__ = "instructions"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    description: Mapped[str] = mapped_column()
    ingredients: Mapped[list[Ingredient]] = relationship(secondary=instructions_to_ingredients,
                                                         back_populates="instructions")
    time: Mapped[int] = mapped_column()  # minutes that instruction takes

    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.id"))
    recipe: Mapped["Recipe"] = relationship(back_populates="instructions")

    def to_domain(self) -> DomainInstruction:
        return TimeStep(
            id=self.id,
            title=self.description,
            ingredients=[ingredient.to_domain() for ingredient in self.ingredients],
            timer=self.time,
            recipe_id=self.recipe_id,
        )

    @classmethod
    def from_domain(cls, instruction: DomainInstruction) -> "Instruction":
        if not isinstance(instruction, TimeStep):
            raise NotImplementedError

        return cls(
            id=instruction.id,
            description=instruction.title,
            ingredients=[Ingredient.from_domain(ingredient) for ingredient in instruction.ingredients],
            time=instruction.timer,
        )


class Recipe(Base):
    __tablename__ = "recipes"
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)

    title: Mapped[str] = Column(String)
    description: Mapped[str] = Column(String)
    instructions: Mapped[list[Instruction]] = relationship(back_populates="recipe")

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner: Mapped[User] = relationship(back_populates="recipes")

    def to_domain(self) -> DomainRecipe:
        return DomainRecipe(
            id=self.id,
            title=self.title,
            description=self.description,
            owner=self.owner.to_domain(),
            tags=[],
            additional_info=RecipeAdditionalInformation(
                prep_time=0,
                work_time=0,
                servings=1,
            ),
            ingredients=[instruction.to_domain() for instruction in self.instructions],
        )

    @classmethod
    def from_domain(cls, domain_recipe: DomainRecipe) -> "Recipe":
        return cls(
            id=domain_recipe.id,
            title=domain_recipe.title,
            description=domain_recipe.description,
            instructions=[
                Instruction.from_domain(instruction) for instruction in domain_recipe.instructions
            ],
            owner_id=domain_recipe.owner.id,
        )

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from DB.template import Base


class FieldModel(Base):
    __tablename__ = "fields"
    id = Column(Integer, primary_key=True, index=True)
    section_id = Column(Integer, ForeignKey("sections.id"))
    field_name = Column(String)
    field_rename = Column(String)
    field_type = Column(String)
    field_is_active = Column(Boolean)


class SectionModel(Base):
    __tablename__ = "sections"
    id = Column(Integer, primary_key=True, index=True)
    tab_id = Column(Integer, ForeignKey("tabs.id"))
    section_name = Column(String)
    section_rename = Column(String)
    section_is_active = Column(Boolean)
    section_fields = relationship("FieldModel", back_populates="section")


class TabModel(Base):
    __tablename__ = "tabs"
    id = Column(Integer, primary_key=True, index=True)
    template_id = Column(Integer, ForeignKey("templates.id"))
    tab_name = Column(String)
    tab_rename = Column(String)
    tab_is_active = Column(Boolean)
    tab_sections = relationship("SectionModel", back_populates="tab")


class TemplateModel(Base):
    __tablename__ = "templates"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    rename = Column(String)
    tabs = relationship("TabModel", back_populates="template")


FieldModel.section = relationship(
    "SectionModel", back_populates="section_fields")
SectionModel.tab = relationship("TabModel", back_populates="tab_sections")
TabModel.template = relationship("TemplateModel", back_populates="tabs")
# Base.metadata.create_all(bind=engine)

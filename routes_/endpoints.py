from fastapi import Depends, APIRouter
# from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import models.template
from sqlalchemy.orm import Session, joinedload
from schemas.template import Template
from typing import List
from DB.template import SessionLocal, engine
appp = APIRouter()
models.template.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# db_dependency=Annotated[Session,De]


@appp.post("/create_template")
async def create_template(template: Template, db: Session = Depends(get_db)):
    template_model = models.template.TemplateModel(
        name=template.name, rename=template.rename)
    db.add(template_model)
    db.commit()
    db.refresh(template_model)

    for tab in template.tabs:
        tab_model = models.template.TabModel(
            template_id=template_model.id,
            tab_name=tab.tab_name,
            tab_rename=tab.tab_rename,
            tab_is_active=tab.tab_is_active
        )
        db.add(tab_model)
        db.commit()
        db.refresh(tab_model)

        if tab.tab_sections:
            for section in tab.tab_sections:
                section_model = models.template.SectionModel(
                    tab_id=tab_model.id,
                    section_name=section.section_name,
                    section_rename=section.section_rename,
                    section_is_active=section.section_is_active
                )
                db.add(section_model)
                db.commit()
                db.refresh(section_model)

                for field in section.section_fields:
                    field_model = models.template.FieldModel(
                        section_id=section_model.id,
                        field_name=field.field_name,
                        field_rename=field.field_rename,
                        field_type=field.field_type,
                        field_is_active=field.field_is_active
                    )
                    db.add(field_model)
                    db.commit()
                    db.refresh(field_model)

    return {"msg": "Template created successfully", "id": template_model.id}


# @appp.get("/templates")
# async def get_templates(db: Session = Depends(get_db)):
#     result = db.execute(select(models.template.TemplateModel))
#     templates = result.scalars().all()
#     return templates

@appp.get("/templates", response_model=List[Template])
def get_templates(db: Session = Depends(get_db)):
    templates = db.query(models.template.TemplateModel).options(
        joinedload(models.template.TemplateModel.tabs)
        .joinedload(models.template.TabModel.tab_sections)
        .joinedload(models.template.SectionModel.section_fields)
    ).all()
    return templates

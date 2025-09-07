from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date

class ContactInfo(BaseModel):
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

class EducationEntry(BaseModel):
    degree: Optional[str] = None
    institution: Optional[str] = None
    start_date: Optional[str] = None   # ISO format: YYYY-MM or YYYY-MM-DD
    end_date: Optional[str] = None
    grade: Optional[str] = None        # GPA, % etc.


class ExperienceEntry(BaseModel):
    job_title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    responsibilities: List[str] = []
    achievements: List[str] = []


class SkillCategory(BaseModel):
    category: Optional[str] = None     # e.g., "Programming", "Cloud"
    items: List[str] = []              # e.g., ["Python", "C++"]


class Certification(BaseModel):
    name: Optional[str] = None
    issuer: Optional[str] = None
    date: Optional[str] = None


class Language(BaseModel):
    name: Optional[str] = None
    proficiency: Optional[str] = None  # e.g., Native, Fluent, Intermediate


class ResumeInfo(BaseModel):
    name: Optional[str] = None
    contact: ContactInfo = ContactInfo()
    summary: Optional[str] = None
    skills: List[SkillCategory] = []
    education: List[EducationEntry] = []
    experiences: List[ExperienceEntry] = []
    certifications: List[Certification] = []
    languages: List[Language] = []
    raw_text: Optional[str] = None     # keep original extracted text for traceability

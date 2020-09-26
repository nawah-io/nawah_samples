import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminBlogNewComponent } from './admin-blog-new.component';

describe('AdminBlogNewComponent', () => {
  let component: AdminBlogNewComponent;
  let fixture: ComponentFixture<AdminBlogNewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AdminBlogNewComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AdminBlogNewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

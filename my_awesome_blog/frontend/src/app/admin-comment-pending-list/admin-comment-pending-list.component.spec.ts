import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminCommentPendingListComponent } from './admin-comment-pending-list.component';

describe('AdminCommentPendingListComponent', () => {
  let component: AdminCommentPendingListComponent;
  let fixture: ComponentFixture<AdminCommentPendingListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AdminCommentPendingListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AdminCommentPendingListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
